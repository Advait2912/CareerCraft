import { Router } from "express";
import {
  signup,
  signin,
  getCurrentUser,
} from "../controllers/auth.controllers.js";
import { verifyJWT } from "../middleware/auth.middleware.js";

const router = Router();

router.post("/signup", signup);
router.post("/signin", signin);
router.get("/me", verifyJWT, getCurrentUser);

export default router;
