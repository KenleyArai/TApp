import React from "react";
import Link from "next/link";
import uuidv1 from "uuid/v1";
import useUser from "../hooks/useUser";
import Router from "next/router";

const signout = setUser => {
  setUser({
    firstname: null,
    lastname: null,
    access_token: null,
    user_id: null
  });
  Router.push("/");
};

const Navbar = ({ links }) => {
  const [accessToken, firstname, lastname, user_id, setUser] = useUser();

  if (accessToken) {
    return (
      <ul>
        <li key={uuidv1()}>
          <Link prefetch href={"/dashboard"}>
            <a>{"Dashboard"}</a>
          </Link>
        </li>
        <li key={uuidv1()}>
          Welcome {firstname} {lastname},{" "}
          <a onClick={() => signout(setUser)}>{"Sign Out"}</a>
        </li>
        <style jsx>{`
          a {
            color: #5e81ac;
            text-decoration: underline;
            cursor: pointer;
          }
          ul {
            display: flex;
            flex-direction: row;
            background-color: #4c566a;
            padding: 1em;
            justify-content: space-between;
          }
        `}</style>
      </ul>
    );
  }
  return (
    <ul>
      <li key={uuidv1()}>
        <Link prefetch href={"/"}>
          <a>{"Home"}</a>
        </Link>
      </li>
      <li key={uuidv1()}>
        <Link prefetch href={"/signup"}>
          <a>{"Sign Up"}</a>
        </Link>
      </li>
      <style jsx>{`
        a {
          color: #88c0d0;
          text-decoration: underline;
          cursor: pointer;
        }
        ul {
          display: flex;
          flex-direction: row;
          background-color: #4c566a;
          padding: 1em;
          justify-content: space-between;
        }
      `}</style>
    </ul>
  );
};

export default Navbar;
