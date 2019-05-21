import React, { useState } from "react";
import useLocalStorage from "../hooks/useLocalStorage";

const sendLogin = (event, email, password, setAccessToken) => {
  event.preventDefault();
  fetch("http://localhost:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      email: email,
      password: password
    })
  })
    .then(resp => {
      if (!resp.ok) throw Error(resp.statusText);
      return resp;
    })
    .then(resp => resp.json())
    .then(resp => setAccessToken(resp["access_token"]))
    .catch(() => console.log("ERROR"));
};

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [accessToken, setAccessToken] = useLocalStorage("accessToken", null);

  if (!accessToken) {
    return (
      <form
        onSubmit={event =>
          sendLogin(event, email, password, setLogin, setAccessToken)
        }
      >
        <label>
          Email:
          <input
            type="text"
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          Password:
          <input
            type="text"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
          />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
  return <div>You are logged in!</div>;
};

export default Login;
