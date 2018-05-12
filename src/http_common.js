import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `http://jsonplaceholder.typicode.com/`,
  headers: {
    Authorization: 'Bearer {token}'
  }
});
 
export function getComments(commentid) {
  return HTTP.get(`comments` + '/' + commentid)
  .then(response => response)
  .catch(rerror => rerror);
}

export function cube(x) {
  return x * x * x;
};