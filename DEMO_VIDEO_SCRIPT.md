# API Demo Video Script (4 minutes)

## Setup Before Recording

**Have these ready:**
1. ✅ Server running: `python manage.py runserver`
2. ✅ Terminal window open
3. ✅ Browser at http://localhost:8000/api/
4. ✅ Token ready (see Part 1 first)

---

## 📹 INTRO (30 seconds)

**Say:**
> "Hi, I'm [Your Name]. This is an Inventory Management API I built for my capstone project. It's a REST API that lets teams manage products and automatically tracks every change. Let me show you how it works."

**Show:** Browser at `http://localhost:8000/api/`

---

## 🔐 PART 1: GET A TOKEN (45 seconds)

**Say:**
> "To create products, I need a token. The API uses token authentication for security."

**In terminal:**
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Copy the token you get back. You'll use it next.**

---

## ✨ PART 2: CREATE & VIEW A PRODUCT (1 minute 15 seconds)

**Say:**
> "Now let me create a product using my token."

**In terminal (replace YOUR_TOKEN):**
```bash
curl -X POST http://localhost:8000/api/products/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Wireless Mouse", "category": 1, "quantity": 50, "price": "29.99"}'
```

**Say:**
> "Great! I created a product. Now let me search for it."

**In browser, go to:**
```
http://localhost:8000/api/products/?search=mouse
```

**Say:**
> "I can search by name. The API found my mouse."

---

## 📊 PART 3: UPDATE & SHOW AUDIT TRAIL (1 minute 15 seconds)

**Say:**
> "Here's the key feature—when I update the quantity, the system automatically logs who changed it and when."

**In terminal:**
```bash
curl -X PATCH http://localhost:8000/api/products/1/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"quantity": 45}'
```

**Say:**
> "I updated the quantity from 50 to 45. Now let me show the change history."

**In browser:**
```
http://localhost:8000/api/inventory-changes/
```

**Say:**
> "Perfect! The system logged the change—showing the old quantity, new quantity, who made it, and when. This is perfect for auditing."

---

## 📝 OUTRO (30 seconds)

**Say:**
> "So that's my API. It lets users view products publicly, authenticated users can create and edit, and every change is tracked automatically. The code is on GitHub with full documentation. Thanks for watching!"

---

## ⏱️ Timing

- Intro: 30 sec
- Get token: 45 sec
- Create & search: 1 min 15 sec
- Update & audit: 1 min 15 sec
- Outro: 30 sec

**Total: 4 minutes exactly**

---

## 🎥 Quick Tips

1. **Move slowly** — let viewers read the terminal output
2. **One window at a time** — switch between terminal and browser clearly
3. **Pause after results** — show each API response for 2-3 seconds
4. **Speak naturally** — use the script as a guide, not a script to read

---

## 🚨 If Something Goes Wrong

**Server not running?**
```bash
python manage.py runserver
```

**Token invalid?**
Get a fresh one using the curl command in Part 1.

**Product already exists?**
Use a different name like "Keyboard" or "USB Cable" instead.

---

## 💡 Pro Tips for Great Demo

1. **Move slowly** — give viewers time to read what's on screen
2. **Narrate what you're doing** — "I'm going to search for products with low stock"
3. **Show real data** — the products and changes you created are more convincing than empty lists
4. **Highlight the key feature** — the automatic change tracking is the coolest part, spend time on that
5. **End strong** — remind them it's on GitHub and they can clone it

---

**Last Updated:** January 4, 2026  
**Ready to Record:** Yes ✅
