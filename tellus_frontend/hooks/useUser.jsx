import React from "react";
import useLocalStorage from "./useLocalStorage";

const useUser = () => {
  const [accessToken, setAccessToken] = useLocalStorage("accessToken", null);
  const [firstname, setFirstname] = useLocalStorage("firstname", null);
  const [lastname, setLastname] = useLocalStorage("lastname", null);
  const [user_id, setUser_ID] = useLocalStorage("user_id", null);

  const setUser = user => {
    setAccessToken(user["access_token"]);
    setFirstname(user["firstname"]);
    setLastname(user["lastname"]);
    setUser_ID(user["user_id"]);
  };

  return [accessToken, firstname, lastname, user_id, setUser];
};

export default useUser;
