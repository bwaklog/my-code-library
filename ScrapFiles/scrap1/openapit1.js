import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
    organization: "org-gWIvDmKnAp5G43BbteQFjQ7u",
    apiKey: process.env."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",
});
const openai = new OpenAIApi(configuration);
const response = await openai.listEngines();