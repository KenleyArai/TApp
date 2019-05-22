import React, { useState } from "react";
import useUser from "../hooks/useUser";
import Router from "next/router";

const sendLogin = (event, email, password, setUser, setError) => {
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
      if (!resp.ok) {
        resp.json().then(obj => setError(obj.msg));
        throw Error(resp.statusText);
      }
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
  const [errorCheck, setError] = useState(true);
  if (!accessToken) {
    return (
      <div>
        <form
          onSubmit={event =>
            sendLogin(event, email, password, setUser, setError)
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
        {errorCheck ? errorCheck : ""}
      </div>
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
