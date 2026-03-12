// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Point2Space',
  tagline: 'Interactive math visualization platform',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://provility.github.io',
  baseUrl: '/p2s-docs/',

  organizationName: 'provility',
  projectName: 'p2s-docs',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'light',
        disableSwitch: true,
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'Point2Space',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'expressionsSidebar',
            label: 'Expressions',
            position: 'left',
          },
          {
            type: 'docSidebar',
            sidebarId: 'toolbarSidebar',
            label: 'Toolbar',
            position: 'left',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} Point2Space.`,
      },
      prism: {
        theme: prismThemes.github,
      },
      codeBlock: {
        showCopyButton: true,
      },
    }),
};

export default config;
