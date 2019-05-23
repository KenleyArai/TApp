import React from "react";
import Head from "next/head";

export default () => (
  <div>
    <Head>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta charSet="utf-8" />
      <link
        href="https://fonts.googleapis.com/css?family=Open+Sans|Pacifico&display=swap"
        rel="stylesheet"
      />
    </Head>
    <style jsx global={true}>{`
      html {
        box-sizing: border-box;
        font-family: "Open Sans", sans-serif;
      }

      *,
      *: before,
      *: after {
        box-sizing: inherit;
      }

      body,
      h1,
      h2,
      h3,
      ul,
      li,
      p,
      pre,
      figure,
      hr {
        margin: 0;
        padding: 0;
      }

      h1,
      h2,
      h3 {
        font-family: "Pacifico", cursive;
      }

      body {
        background-color: #d8dee9;
      }

      ul,
      li {
        list-style: none;
      }

      input,
      textarea,
      select,
      button {
        color: inherit;
        font: inherit;
        letter-spacing: inherit;
      }

      button {
        border-radius: 0;
        padding: 0.75em 1em;
        background-color: transparent;
      }

      button * {
        pointer-events: none;
      }

      img,
      object {
        display: block;
        max-width: 100 %;
      }
    `}</style>
  </div>
);
