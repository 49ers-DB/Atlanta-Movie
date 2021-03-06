export const customerRegister = user => {
    let url = process.env.REACT_APP_API_URL
    return fetch(url + "/customerRegister", {
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
        console.log(data)
  
      } else {
        // localStorage.setItem("token", data.jwt)
        // dispatch(loginUser(data.user))
        console.log("Registered")
        return data;
      }
    })
  }

  export default customerRegister;