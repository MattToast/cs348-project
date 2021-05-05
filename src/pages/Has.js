import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Has extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hasList: []
    }
  }

  componentDidMount() {
    fetch('/api/has')
      .then(res => res.json())
      .then(data => this.setState({ hasList: data }));
  }

  render() {
    const manyHas = this.state.hasList;
    return (
      <div>
        <div>
          <NewHasForm />
        </div>
        <div>
          {
            manyHas.map((has) => {
              return (<ObjectCard data={has} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Has;
