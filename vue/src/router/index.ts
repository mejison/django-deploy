import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'

import store from '../store'

import Product from '../views/Product.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import CreateAuction from '../views/CreateAuction.vue'
import MyAuctions from '../views/MyAuctions.vue'
import MyProduct from '../views/MyProduct.vue'
import Search from '../views/Search.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path:'/question',
    name: 'Question',
    component: Product

  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path:'/my-product/:product_slug',
    name: 'Question',
    component: MyProduct

  },
  {
    path: '/getquestion/:product_slug',
    name: 'GetQuestion',
    component: MyProduct
  },
  {
    path: '/sendmail/:product_slug',
    name: 'GetQuestion1',
    component: Product
  },
  //{
  //  path: '/getanswer/:product_slug',
  //  name: 'GetQuestion',
  //  component: MyProduct
  //},
  {
    path: '/answer',
    name: 'Answer',
    component: MyProduct
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/create-auction',
    name: 'CreateAuction',
    component: CreateAuction

  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/:product_slug/',
    name: 'Product1',
    component: Product
  },
  {
    path: '/bid',
    name: 'Product',
    component: Product
  },
  {
    path: '/my-auction',
    name: 'MyAuction',
    component: MyAuctions
  }
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
