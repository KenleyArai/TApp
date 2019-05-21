import React, { useState } from "react";

const sendLogin = (event, username, password, setLogin) => {
  event.preventDefault();
  fetch("http://localhost:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: username,
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
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [LoggedIn, setLogin] = useState(false);

  if (!LoggedIn) {
    return (
      <form onSubmit={event => sendLogin(event, username, password, setLogin)}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={e => setUsername(e.target.value)}
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
