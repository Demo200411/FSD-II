import { createStore } from "redux";
import { CounterReducer } from "./CounterReducer";

// pass this store to Provider in main.jsx
export const store = createStore(CounterReducer);