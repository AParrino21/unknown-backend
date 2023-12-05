const router = require("express").Router();
const unknownMobileRoutes = require('./unknownMobileRoutes')

router.use("/unknownM", unknownMobileRoutes);

module.exports = router;