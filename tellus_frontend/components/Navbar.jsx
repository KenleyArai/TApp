import React from "react";
import Link from "next/link";
import uuidv1 from "uuid/v1";

const Navbar = ({ links }) => {
  return (
    <ul>
      {links.map(link => (
        <li key={uuidv1()}>
          <Link prefetch href={link.href}>
            <a>{link.text}</a>
          </Link>
        </li>
      ))}
    </ul>
  );
};

export default Navbar;
