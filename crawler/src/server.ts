import { readFile } from "fs/promises";
import express, { Express } from "express";
import { PathLike } from "fs";
import { Config, configSchema } from "./config.js";
import { configDotenv } from "dotenv";
import cors from "cors";
import CrawlerManager from "./core.js";

configDotenv();

const app: Express = express();
const listeningPort = Number(process.env.API_PORT) || 3000;
const host = process.env.API_HOST || "localhost";

app.use(cors());
app.use(express.json());

app.post("/crawl", async (req, res) => {
  const config: Config = req.body;
  try {
    const currentConfig = configSchema.parse(config);
    const crawler = new CrawlerManager(currentConfig);
    await crawler.crawl();
    const outputFile: PathLike = await crawler.write();
    const content = await readFile(outputFile, "utf-8");
    res.contentType("application/json");
    return res.send(content);
  } catch (error) {
    return res
      .status(500)
      .json({ message: "Error occurred during crawling", error });
  }
});

app.listen(listeningPort, host, () => {
  console.log(`listening at http://${host}:${listeningPort}`);
});

export default app;
