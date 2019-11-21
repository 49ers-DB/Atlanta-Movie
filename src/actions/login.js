export const userLogin = user => {
    let url = process.env.REACT_APP_API_URL
    return fetch(url + "/userLogin", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify({user})
    });
  }

  export default userLogin;