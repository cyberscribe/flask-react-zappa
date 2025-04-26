const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin   = require('css-minimizer-webpack-plugin');
const TerserPlugin         = require('terser-webpack-plugin');

module.exports = (env, argv) => ({
  entry: {
    app:   './assets/ts/main.ts',
    style: './assets/scss/main.scss'
  },
  output: {
    filename: 'js/[name].js',
    path:     path.resolve(__dirname, 'static'),
    publicPath: '/static/'
  },
  mode: argv.mode || 'development',
  devtool: argv.mode === 'development' ? 'source-map' : false,
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
           MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader'
        ]
      }
    ]
  },
  resolve: { extensions: ['.ts','.tsx','.js'] },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].css',
    })
  ],
  optimization: {
    minimize: argv.mode === 'production',
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: argv.mode === 'production'
          }
        }
      }),
      new CssMinimizerPlugin()
    ],
  }
});