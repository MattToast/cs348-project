import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Hompage from './pages/Hompage';
import Customers from './pages/Customers';
import Employees from './pages/Employees';
import Inventory from './pages/Inventory';
import Locations from './pages/Locations';
import Sales from './pages/Sales';
import Transfers from './pages/Transfers';
import Includes from './pages/Includes';
import Has from './pages/Has';
import Buys from './pages/Buys';

class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Hompage} />
          <Route path="/locations" component={Locations} />
          <Route path="/employee" component={Employees} />
          <Route path="/inventory" component={Inventory} />
          <Route path="/sales" component={Sales} />
          <Route path="/customers" component={Customers} />
          <Route path="/transfers" component={Transfers} />
          <Route path="/includes" component={Includes} />
          <Route path="/has" component={Has} />
          <Route path="/buys" component={Buys} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
