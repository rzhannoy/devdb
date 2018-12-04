import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'message/',
    headers: conf.headers,
  })

  return resource
}
