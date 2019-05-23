import React, { useState } from "react";
import useUser from "../hooks/useUser";
import Router from "next/router";
import FormInput from "./FormInput";

const checkPassword = (password, confirmPassword) =>
  password === confirmPassword;

const sendSignUp = (
  event,
  email,
  firstname,
  lastname,
  password,
  confirmPassword,
  setError,
  setUser
) => {
  event.preventDefault(); // Stops from submitting to a new page
  if (!checkPassword(password, confirmPassword)) {
    setError("Emails do not match");
  } else {
    fetch("http://localhost:5000/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email,
        password: password,
        firstname: firstname,
        lastname: lastname
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
  }
};

const SignUpForm = () => {
  const [email, setEmail] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorCheck, setError] = useState(true);
  const [accessToken, fn, ls, user_id, setUser] = useUser();

  return (
    <div>
      <form
        onSubmit={event =>
          sendSignUp(
            event,
            email,
            firstname,
            lastname,
            password,
            confirmPassword,
            setError,
            setUser
          )
        }
      >
        <FormInput title={"Email"} value={email} onChange={setEmail} />
        <FormInput
          title={"First Name"}
          value={firstname}
          onChange={setFirstname}
        />
        <FormInput
          title={"Last Name"}
          value={lastname}
          onChange={setLastname}
        />
        <FormInput title={"Password"} value={password} onChange={setPassword} />
        <FormInput
          title={"Confrim Password"}
          value={confirmPassword}
          onChange={setConfirmPassword}
        />
        <input type="submit" value="Submit" />
      </form>
      {errorCheck ? errorCheck : ""}
    </div>
  );
};

export default SignUpForm;
