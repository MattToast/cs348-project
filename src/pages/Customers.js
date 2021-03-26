import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Customers extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      customersList: []
    }
  }

  componentDidMount() {
    fetch('/api/customers')
      .then(res => res.json())
      .then(data => this.setState({ customersList: data }));
  }

  render() {
    const custs = this.state.customersList;
    return (
      <div>
      <div>
        TODO - Still up for debate if adding is a manual proccess or if it should happen automatically on first sale
      </div>
      <div>
        {
          custs.map((cust) => {
            return (<ObjectCard data={cust}/>);
          })
        }
      </div>
      </div>
    );
  }
}

export default Customers;
