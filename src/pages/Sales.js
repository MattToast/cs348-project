import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Sales extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      salesList: []
    }
  }

  componentDidMount() {
    fetch('/api/sales')
      .then(res => res.json())
      .then(data => this.setState({ salesList: data }));
  }

  render() {
    const sales = this.state.salesList;
    return (
      <div>
        {
          sales.map((sale) => {
            return (<ObjectCard data={sale}/>);
          })
        }
      </div>
    );
  }
}

export default Sales;
