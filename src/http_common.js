import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `http://localhost:8000`,
  headers: {
    Authorization: 'Bearer {token}'
  }
});
 
export function getBlogs(commentid) {
  if (commentid) {
    return HTTP.get('blog',{params:{id:commentid}})
    .then(response => response)
    .catch(rerror => rerror);
  } else {
  return HTTP.get('blogs')
  .then(response => response)
  .catch(rer => rerror);
  }
}

export function cube(x) {
  return x * x * x;
};