const router = require("express").Router();
require("dotenv").config();

router.post("/createUser", (req, res) => {
  fetch(
    `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=${process.env.KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(req.body),
    }
  )
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      return res.json(data);
    });
});

router.post("/login", (req, res) => {
  fetch(
    `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=${process.env.KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(req.body),
    }
  )
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      return res.json(data);
    });
});

module.exports = router;
