module.exports = {
  devServer: {
    proxy: {
      '/media': { target: 'http://127.0.0.1:8000/media' },
    },
  },
}
