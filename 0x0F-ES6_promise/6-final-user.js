#!/usr/bin/node
import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

async function handleProfileSignup(firstName, lastName, fileName) {
  const Promi_1 = {
    status: "pending ",
  };
  const Promi_2 = {
    status: "pending ",
  };

  try {
    const signup = await signUpUser(firstName, lastName);
    Promi_1.status = "fulfilled";
    Promi_1.value = signup;
  } catch (err) {
    Promi_1.status = "rejected";
    Promi_1.value = err.toString();
  }

  try {
    const upload = await uploadPhoto(fileName);
    Promi_2.status = "fulfilled";
    Promi_2.value = upload;
  } catch (err) {
    Promi_2.status = "rejected";
    Promi_2.value = err.toString();
  }

  return [Promi_1, Promi_2];
}

export default handleProfileSignup;
