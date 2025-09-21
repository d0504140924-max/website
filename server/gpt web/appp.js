// app.js — דף ניהול שמכסה את כל המסלולים בקובץ server_abstract.py
console.log("Admin full loaded");

const baseUrlEl = document.getElementById("baseUrl");
const tokenEl   = document.getElementById("token");
const routeEl   = document.getElementById("routeSelect");
const methodBox = document.getElementById("methodBox");
const fieldsEl  = document.getElementById("paramFields");
const useRawEl  = document.getElementById("useRawJSON");
const rawJsonEl = document.getElementById("rawJSON");
const outputEl  = document.getElementById("output");
const sendBtn   = document.getElementById("sendBtn");
const clearBtn  = document.getElementById("clearBtn");

// הגדרות כל המסלולים (שם, method, וסכמת שדות מוצעת)
// ניתן לשנות שמות פרמטרים לפי ההטמעה אצלך בצד שרת
const ROUTES = [
  // GET
  { key:"Category",        method:"GET",  path:"/api/Category",        params:[ /* אולי name? */ ] },
  { key:"ShoeAll",         method:"GET",  path:"/api/ShoeAll",         params:[ ] },
  { key:"ItemDetail",      method:"GET",  path:"/api/ItemDetail",      params:[ {key:"item_id", label:"מזהה פריט", type:"text"} ] },
  { key:"ShowMoneyStatus", method:"GET",  path:"/api/ShowMoneyStatus", params:[ ] },
  { key:"GetAmount",       method:"GET",  path:"/api/GetAmount",       params:[ {key:"item_id", label:"מזהה פריט", type:"text"} ] },
  { key:"MonthReport",     method:"GET",  path:"/api/MonthReport",     params:[ {key:"month", label:"חודש (YYYY-MM)", type:"month"} ] },
  { key:"MovementRecord",  method:"GET",  path:"/api/MovementRecord",  params:[ {key:"item_id", label:"מזהה (לא חובה)", type:"text", optional:true},
                                                                                {key:"from_date", label:"מתאריך (YYYY-MM-DD)", type:"date", optional:true},
                                                                                {key:"to_date",   label:"עד תאריך (YYYY-MM-DD)", type:"date", optional:true} ] },
  // POST
  { key:"ChangePrice",     method:"POST", path:"/api/ChangePrice",     params:[ {key:"item_id", label:"מזהה פריט", type:"text"},
                                                                                {key:"new_price", label:"מחיר חדש", type:"number", step:"0.01"} ] },
  { key:"AddItem",         method:"POST", path:"/api/AddItem",          params:[ {key:"name", label:"שם פריט", type:"text"},
                                                                                {key:"category", label:"קטגוריה", type:"text"},
                                                                                {key:"price", label:"מחיר", type:"number", step:"0.01"},
                                                                                {key:"qty", label:"כמות התחלתית", type:"number", step:"1"} ] },
  { key:"RemoveItem",      method:"POST", path:"/api/RemoveItem",       params:[ {key:"item_id", label:"מזהה פריט", type:"text"} ] },
  { key:"DepositMoney",    method:"POST", path:"/api/DepositMoney",     params:[ {key:"amount", label:"סכום להפקדה", type:"number", step:"0.01"} ] },
  { key:"WithdrawMoney",   method:"POST", path:"/api/WithdrawMoney",    params:[ {key:"amount", label:"סכום למשיכה", type:"number", step:"0.01"} ] },
];

function initRoutes(){
  for(const r of ROUTES){
    const opt = document.createElement("option");
    opt.value = r.key;
    opt.textContent = `${r.method} ${r.path}`;
    routeEl.appendChild(opt);
  }
  routeEl.value = ROUTES[0].key;
  syncRouteUI();
}

function syncRouteUI(){
  const r = currentRoute();
  methodBox.value = r.method;
  renderParams(r);
  useRawEl.checked = false;
  rawJsonEl.classList.add("hidden");
}

function currentRoute(){
  const key = routeEl.value;
  return ROUTES.find(r => r.key === key);
}

function renderParams(route){
  fieldsEl.innerHTML = "";
  if(!route.params || route.params.length === 0){
    const p = document.createElement("p");
    p.className = "muted";
    p.textContent = "אין פרמטרים נדרשים לפעולה זו.";
    fieldsEl.appendChild(p);
    return;
  }
  for(const f of route.params){
    const wrap = document.createElement("label");
    wrap.innerHTML = `${f.label}${f.optional ? " (אופציונלי)" : ""}
      <input id="param_${f.key}" ${f.type ? `type="${f.type}"` : ""} ${f.step ? `step="${f.step}"` : ""}/>`;
    fieldsEl.appendChild(wrap);
  }
}

routeEl.addEventListener("change", syncRouteUI);
useRawEl.addEventListener("change", () => {
  const r = currentRoute();
  if(r.method !== "POST"){
    useRawEl.checked = false;
    alert("JSON גולמי רלוונטי רק ל־POST.");
    return;
  }
  rawJsonEl.classList.toggle("hidden", !useRawEl.checked);
});

clearBtn.addEventListener("click", () => {
  outputEl.textContent = "{ }";
});

sendBtn.addEventListener("click", async () => {
  const base = (baseUrlEl.value || "").replace(/\/+$/g, "");
  const token = tokenEl.value || "";
  const r = currentRoute();

  let url = base + r.path;
  let init = { method: r.method, headers: {} };

  if(r.method === "GET"){
    // build query string
    const qp = new URLSearchParams();
    for(const f of (r.params || [])){
      const el = document.getElementById(`param_${f.key}`);
      if(!el) continue;
      const v = el.value;
      if(v === "" && f.optional) continue;
      qp.set(f.key, v);
    }
    const qs = qp.toString();
    if(qs) url += "?" + qs;
  } else {
    // POST
    init.headers["Content-Type"] = "application/json";
    let bodyObj = {};

    if(useRawEl.checked){
      try{
        bodyObj = JSON.parse(rawJsonEl.value || "{}");
      }catch(e){
        outputEl.textContent = JSON.stringify({ ok:false, error:"JSON שגוי", details:String(e) }, null, 2);
        return;
      }
    }else{
      for(const f of (r.params || [])){
        const el = document.getElementById(`param_${f.key}`);
        if(!el) continue;
        let v = el.value;
        if(f.type === "number" && v !== "") v = Number(v);
        if(v === "" && f.optional) continue;
        bodyObj[f.key] = v;
      }
    }

    // הכנסנו תמיכה באסימון אם צריך בצד שרת
    if(token) bodyObj.token = token;
    init.body = JSON.stringify(bodyObj);
  }

  outputEl.textContent = "מבצע בקשה...";
  try{
    const res = await fetch(url, init);
    const text = await res.text();
    let data;
    try { data = JSON.parse(text); } catch { data = { raw: text }; }

    outputEl.textContent = JSON.stringify({
      ok: res.ok,
      status: res.status,
      url, method: r.method,
      response: data
    }, null, 2);
  }catch(err){
    outputEl.textContent = JSON.stringify({ ok:false, error:String(err) }, null, 2);
  }
});

// start
initRoutes();
