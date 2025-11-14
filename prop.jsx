////////////////////////App.jsx

import React from "react";
import Welcome from "./Welcome";
function App() {
return (
<div style={{ fontFamily: "system-ui", padding: 20 }}>
<h2>React Props and State Example</h2>
{/* Pass data (props) to child component */}
<Welcome name="Alice" />
<Welcome name="Bob" />
</div>
);
}
export default App 

////////////////////////////////////Welcome.jsx

import React, { useState } from "react";
function Welcome({ name }) {
const [count, setCount] = useState(0);
return (
<div
style={{
border: "1px solid #ccc",
padding: "10px",
margin: "10px 0",
borderRadius: "8px",
}}
>
<h3>Hello, {name}  </h3>
<p>You have greeted {count} times.</p>
<button onClick={() => setCount(count + 1)}>Say Hello</button>
</div>
);
}
export default Welcome; 

/////////////////////////////////main.jsx

import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
const root = createRoot(document.getElementById("root"));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);

/////////////////////////////////index.html

<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/svg+xml" href="/vite.svg" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Prop</title>
</head>

<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>

</html>
