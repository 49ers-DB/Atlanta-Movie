export const userRegister = user => {
    let url = process.env.REACT_APP_API_URL
    return fetch(url + "/userRegister", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify({user})
    })
    .then(resp => resp.json())
    .then(data => {
      if (data.message) {
        // Here you should have logic to handle invalid login credentials.
        // This assumes your Rails API will return a JSON object with a key of
        // 'message' if there is an error
        console.error("Bad Register parameters")
        window.alert(data.message)
        return data
  
      } else {
        // localStorage.setItem("token", data.jwt)
        // dispatch(loginUser(data.user))
        window.alert("Registered")
        window.location.replace("/")
        return data;
      }
    })
  }

  export default userRegister;