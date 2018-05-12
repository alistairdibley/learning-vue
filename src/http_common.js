import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `http://jsonplaceholder.typicode.com/`,
  headers: {
    Authorization: 'Bearer {token}'
  }
});
 
export function getComments(commentid) {
  if (commentid) {
    return HTTP.get('photos/' + commentid)
    .then(response => response)
    .catch(rerror => rerror);
  } else {
  return HTTP.get('photos')
  .then(response => response)
  .catch(rer => rerror);
  }
}

export function cube(x) {
  return x * x * x;
};