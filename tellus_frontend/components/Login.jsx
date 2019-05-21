import React, { useState } from "react";
import useUser from "../hooks/useUser";
import Router from "next/router";

const sendLogin = (event, email, password, setUser) => {
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
    .then(resp => setUser(resp))
    .then(() => Router.push("/dashboard"))
    .catch(() => console.log("ERROR"));
};

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [accessToken, firstname, lastname, user_id, setUser] = useUser();

  if (!accessToken) {
    return (
      <form onSubmit={event => sendLogin(event, email, password, setUser)}>
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
  return (
    <div>
      <h3>
        Hello {firstname} {lastname}
      </h3>
    </div>
  );
};

export default Login;
