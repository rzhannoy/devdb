import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'skill-group/',
    headers: conf.headers,
  })

  return resource
}
