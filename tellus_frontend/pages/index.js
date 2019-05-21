import Page from "../components/Page";
import Login from "../components/Login";
function Home() {
  return (
    <Page bannerText={"home"}>
      <Login />
    </Page>
  );
}

export default Home;
