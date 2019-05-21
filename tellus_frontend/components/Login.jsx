import React, { useState } from "react";

const sendLogin = (event, email, password, setLogin) => {
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
    .then(resp => console.log(resp))
    .then(() => setLogin(true))
    .catch(() => console.log("ERROR"));
};

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [LoggedIn, setLogin] = useState(false);

  if (!LoggedIn) {
    return (
      <form onSubmit={event => sendLogin(event, email, password, setLogin)}>
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
