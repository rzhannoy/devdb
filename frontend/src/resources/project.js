import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'project/',
    headers: conf.headers,
  })

  return resource
}
