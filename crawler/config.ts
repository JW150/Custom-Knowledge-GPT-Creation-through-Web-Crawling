
        import { Config } from "./src/config";

        export const defaultConfig: Config = {
        url: "https://www.rabbit.tech/",
        match: "https://www.rabbit.tech/**",
        exclude: "*://*/career*",
        maxPagesToCrawl: 50,
        outputFileName: "output.json",
        maxTokens: 200000000,
        };
        