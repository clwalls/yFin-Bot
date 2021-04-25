// index.js

/**
 * Required External Modules
 */
const express = require("express");
const path = require("path");
const { quote } = require("yahoo-finance");
const yahooFinance = require("yahoo-finance");
const yahoo = require("yahoo-financial-data");

//const bot = require("./bot.js");

/**
 * App Variables
 */
const app = express();
const port = process.env.PORT || "8000";

/** Router Example for Defactoring Later on */
// const router = express.Router();
// router.get("/messages", (req, res) => {
//   console.log("show some emssages or whatever..");
//   res.end();
// });
// app.use(router);

/**
 *  App Configuration
 */

const result = yahooFinance.quote("TSLA");

/**
 * Routes Definitions
 */
app.get("/", (req, res) => {
  res.status(200).send(`testing: ${result}`);
});

/**
 * Server Activation
 */
app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});
