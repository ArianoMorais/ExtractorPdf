/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Inclui todos os arquivos HTML em templates e subdiretórios
    './core/templates/**/*.html', // Caso tenha subpastas específicas para templates
    './**/*.py', // Inclui arquivos Python para garantir que Tailwind capture as classes geradas por Django
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}