# React-shop-cloudfront

This is frontend starter project for nodejs-aws mentoring program. It uses the following technologies:

- [Vite](https://vitejs.dev/) as a project bundler
- [React](https://beta.reactjs.org/) as a frontend framework
- [React-router-dom](https://reactrouterdotcom.fly.dev/) as a routing library
- [MUI](https://mui.com/) as a UI framework
- [React-query](https://react-query-v3.tanstack.com/) as a data fetching library
- [Formik](https://formik.org/) as a form library
- [Yup](https://github.com/jquense/yup) as a validation schema
- [Vitest](https://vitest.dev/) as a test runner
- [MSW](https://mswjs.io/) as an API mocking library
- [Eslint](https://eslint.org/) as a code linting tool
- [Prettier](https://prettier.io/) as a code formatting tool
- [TypeScript](https://www.typescriptlang.org/) as a type checking tool

## Available Scripts

### `start`

Starts the project in dev mode with mocked API on local environment.

### `build`

Builds the project for production in `dist` folder.

### `preview`

Starts the project in production mode on local environment.

### `test`, `test:ui`, `test:coverage`

Runs tests in console, in browser or with coverage.

### `lint`, `prettier`

Runs linting and formatting for all files in `src` folder.

## Deploy usage

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Commands](#commands)
  - [Build Project](#build-project)
  - [Deploy Infrastructure](#deploy-infrastructure)
  - [Invalidate CloudFront Cache](#invalidate-cloudfront-cache)
  - [Destroy Infrastructure](#destroy-infrastructure)
- [Project Structure](#project-structure)
- [License](#license)

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Node.js (>= 14.0.0) and npm are installed.
- Python is installed.
- AWS CLI is installed and configured with the necessary permissions.
- AWS CDK is installed globally.

Install AWS CDK globally:
```sh
npm install -g aws-cdk
```

### Installation

Clone the repository and install the dependencies:
```sh
git clone https://github.com/your-username/my-store-app.git
cd my-store-app
npm install
pip install -r requirements.txt
```

### Configuration

Ensure the following files are correctly configured:

#### `cdk.json`

This file specifies the entry point for your CDK application.

#### `app.py`

This file defines the entry point for your AWS CDK application.

#### `cdk_python_stack.py`

This file defines the CDK stack, including the S3 bucket and CloudFront distribution.

#### `invalidate-cloudfront.js`

This script invalidates the CloudFront cache.

### Commands

#### Build Project

To build the project:
```sh
npm run build
```

#### Deploy Infrastructure

To bootstrap and deploy the AWS infrastructure:

1. **Bootstrap the environment**:
   ```sh
   cdk bootstrap aws://144123381586/us-east-1
   ```

2. **Deploy the stack and invalidate CloudFront cache**:
   ```sh
   npm run deploy
   ```

#### Invalidate CloudFront Cache

To manually invalidate the CloudFront cache:
```sh
npm run cloudfront:invalidate
```

#### Destroy Infrastructure

To destroy the AWS infrastructure:
```sh
npm run cdk:destroy
```

### Project Structure

```
my-store-app/
├── cdk-python/
├── cdk_python_stack.py
├── dist/
├── index.html
├── invalidate-cloudfront.js
├── node_modules/
├── package.json
├── package-lock.json
├── public/
├── README.md
├── src/
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
└── cdk.json
```
