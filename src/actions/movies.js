import APIClient from "../apiClient"

const movies = () => {
  var movies = []
  var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      apiClient.perform("get", '/movies').then( resp => {
        resp.map( movie => {
          var movieName = movie.movName;
          movies.push({value: movieName, label: movieName})
        
        })
      });
    
    }
    return movies;
}

export default (movies)