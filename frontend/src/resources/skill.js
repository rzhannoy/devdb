import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'skill/',
    headers: conf.headers,
  })

  resource.LEVEL_OPTIONS = {
    1: 'Beginner',
    2: 'Intermediate',
    3: 'Advanced',
    4: 'Guru',
  }

  return resource
}
