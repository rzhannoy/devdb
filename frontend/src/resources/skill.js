import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'skill/',
    headers: conf.headers,
  })

  resource.LEVEL_OPTIONS = {
    0: `Don't display`,
    1: '1 year',
    2: '2 years',
    3: '3 years',
    4: '4+ years',
  }

  return resource
}
