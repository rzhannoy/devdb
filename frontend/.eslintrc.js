module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'comma-dangle': 0,
    'padded-blocks': 0,
    'camelcase': 0,
    'object-property-newline': 0,
    'prefer-promise-reject-errors': 0
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
}
