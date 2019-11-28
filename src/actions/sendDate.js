const sendDate = (date) => {
  if (date) {
    return date.toISOString().substring(0,10)
  } 
  return date
}


export default (sendDate);

