const CompressionWebpackPlugin = require('compression-webpack-plugin')

module.exports = {
  outputDir: 'dist/new',
  devServer: {
    proxy: {
      '/media': { target: 'http://127.0.0.1:8000/media' },
    },
  },
  configureWebpack: {
    plugins: [
      new CompressionWebpackPlugin({
        test: /\.(js|css)$/,
      }),
    ],
  },
}
