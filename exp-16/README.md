<<<<<<< HEAD
# exp-16-testing
=======
# Experiment 16 – Full Stack Testing (Backend + Frontend)

## 📌 Objective

To perform testing on:

* Backend APIs using **pytest**
* Frontend functions using **vitest**
* Execute tests via CLI and automate using **GitHub Actions (CI/CD)**

---

## 🛠️ Technologies Used

* Python (Flask)
* Pytest
* JavaScript (Node.js)
* Vitest
* GitHub Actions

---

## 📁 Project Structure

```
unit-testing-practical/
│
├── Testing/
│   ├── Backend/
│   │   ├── app.py
│   │   ├── test_app.py
│   │   └── requirements.txt
│   │
│   └── Frontend/
│       ├── add.js
│       ├── add.test.js
│       ├── package.json
│
├── .github/workflows/
│   └── ci.yml
│
├── screenshots/
│   ├── backend-test.png
│   ├── frontend-test.png
│   └── github-actions.png
│
└── README.md
```

---

## 🔙 Backend Testing (Pytest)

### 📌 Command

```
pytest
```

### ✔ Description

* Tests API endpoint `/add`
* Verifies status code and response JSON

---

## 🔜 Frontend Testing (Vitest)

### 📌 Command

```
npm run test
```

### ✔ Description

* Tests `add(a, b)` function
* Ensures correct output

---

## ⚙️ GitHub Actions (CI/CD)

### ✔ Workflow Features

* Runs automatically on push
* Executes:

  * Backend tests (pytest)
  * Frontend tests (vitest)

---

## 📸 Screenshots

### 🔹 Backend Test Output

![Backend Test](screenshots/backend-test.png)

### 🔹 Frontend Test Output

![Frontend Test](screenshots/frontend-test.png)

### 🔹 GitHub Actions Workflow

![GitHub Actions](screenshots/github-actions.png)

---

## ✅ Result

* Backend tests passed successfully ✔
* Frontend tests passed successfully ✔
* CI/CD pipeline executed successfully ✔

---

## 🎯 Conclusion

This experiment demonstrates:

* Automated testing of backend and frontend
* Integration of testing with CI/CD
* Efficient validation of full stack applications

---
>>>>>>> a4595f1 (Initial commit)
