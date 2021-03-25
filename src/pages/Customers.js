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
        {
          custs.map((cust) => {
            return (<ObjectCard data={cust}/>);
          })
        }
      </div>
    );
  }
}

export default Customers;
