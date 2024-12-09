import { z } from "zod";
import type { Page } from "playwright";
import { configDotenv } from "dotenv";

configDotenv();

const Page: z.ZodType<Page> = z.any();

export const configSchema = z.object({
  url: z.string(),
  match: z.string().or(z.array(z.string())),
  exclude: z.string().or(z.array(z.string())).optional(),
  selector: z.string().optional(),
  maxPagesToCrawl: z.number().int().positive(),
  outputFileName: z.string(),
  cookie: z
    .union([
      z.object({
        name: z.string(),
        value: z.string(),
      }),
      z.array(
        z.object({
          name: z.string(),
          value: z.string(),
        }),
      ),
    ])
    .optional(),
  onVisitPage: z
    .function()
    .args(
      z.object({
        page: Page,
        pushData: z.function().args(z.any()).returns(z.promise(z.void())),
      }),
    )
    .returns(z.promise(z.void()))
    .optional(),
  waitForSelectorTimeout: z.number().int().nonnegative().optional(),
  resourceExclusions: z.array(z.string()).optional(),
  maxFileSize: z.number().int().positive().optional(),
  maxTokens: z.number().int().positive().optional(),
});

export type Config = z.infer<typeof configSchema>;
