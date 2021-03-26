import React from 'react';

import './ObjectCard.css';

class ObjectCard extends React.Component {
  static defaultProps = {
    data: {}
  };
  
  constructor(props) {
    super(props);
    this.state = {};
  }

  __listDataFields() {
    const data = this.props.data;
    return (
      <>
      {
        Object.keys(data).map((field) => {
          return (
            <div>{field}: {data[field]}</div>
          )
        })
      }
      </>
    );
  }

  render() {
    return (
      <div className="card">
        {this.__listDataFields()}
      </div>
    );
  }
}

export default ObjectCard;