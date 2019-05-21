import React from "react";

import Navbar from "./Navbar";
import Meta from "./Meta";
import PageBanner from "./PageBanner";

const Page = ({ bannerText, children }) => (
  <div>
    <Meta />
    <Navbar />
    <PageBanner text={bannerText} />
    <div className={"page"}>{children}</div>
    <style jsx>{`
      .page {
        background-color: #eceff4;
        color: #2e3440;
        width: 80%;
        margin: auto;
      }
    `}</style>
  </div>
);

export default Page;
